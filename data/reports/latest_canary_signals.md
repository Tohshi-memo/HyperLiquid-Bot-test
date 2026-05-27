# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T02:52:21.225907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1656` n `12`; crypto_alt avg `0.0513` n `228`; crypto_major avg `0.0987` n `8`; equity avg `0.0222` n `67`; fx avg `-0.0207` n `6`; index avg `-0.0404` n `23`; metal avg `0.1335` n `18`; unknown avg `-0.4087` n `418`
- 1h: commodity avg `-0.2263` n `12`; crypto_alt avg `-0.6304` n `228`; crypto_major avg `-0.162` n `8`; equity avg `0.0102` n `67`; fx avg `-0.0436` n `6`; index avg `0.052` n `23`; metal avg `0.0567` n `18`; unknown avg `-0.4786` n `418`
- 4h: commodity avg `-0.4405` n `12`; crypto_alt avg `-0.2502` n `228`; crypto_major avg `0.2832` n `8`; equity avg `0.1852` n `67`; fx avg `-0.0791` n `6`; index avg `0.2467` n `23`; metal avg `-0.1228` n `18`; unknown avg `-0.467` n `418`
- 24h: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.5713` n `228`; crypto_major avg `-0.1982` n `8`; equity avg `0.8579` n `67`; fx avg `-0.0887` n `6`; index avg `1.0631` n `23`; metal avg `0.0128` n `18`; unknown avg `0.2916` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
