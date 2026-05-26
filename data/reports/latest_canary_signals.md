# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T05:07:19.759272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1194` n `12`; crypto_alt avg `0.0135` n `228`; crypto_major avg `-0.0106` n `8`; equity avg `-0.109` n `67`; fx avg `-0.0011` n `6`; index avg `-0.0204` n `23`; metal avg `-0.0078` n `18`; unknown avg `-0.1558` n `407`
- 1h: commodity avg `0.1742` n `12`; crypto_alt avg `0.5214` n `228`; crypto_major avg `0.2364` n `8`; equity avg `-0.1136` n `67`; fx avg `-0.0034` n `6`; index avg `0.0068` n `23`; metal avg `-0.2208` n `18`; unknown avg `-0.2389` n `407`
- 4h: commodity avg `0.0941` n `12`; crypto_alt avg `0.2021` n `228`; crypto_major avg `-0.0179` n `8`; equity avg `-0.1037` n `67`; fx avg `-0.0395` n `6`; index avg `0.0376` n `23`; metal avg `-0.4379` n `18`; unknown avg `-0.5575` n `407`
- 24h: commodity avg `0.7654` n `12`; crypto_alt avg `-0.6676` n `228`; crypto_major avg `-1.3772` n `8`; equity avg `-0.6347` n `67`; fx avg `0.0013` n `6`; index avg `0.008` n `23`; metal avg `-0.5311` n `18`; unknown avg `0.2332` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
