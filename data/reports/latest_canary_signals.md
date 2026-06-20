# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T11:22:26.325516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.0863` n `228`; crypto_major avg `-0.0107` n `8`; equity avg `0.0338` n `78`; fx avg `0.0041` n `6`; index avg `-0.0005` n `23`; metal avg `0.005` n `18`; unknown avg `-0.1333` n `687`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `-0.2971` n `228`; crypto_major avg `-0.102` n `8`; equity avg `-0.0558` n `78`; fx avg `0.0074` n `6`; index avg `0.0007` n `23`; metal avg `0.0127` n `18`; unknown avg `-0.3459` n `687`
- 4h: commodity avg `-0.1242` n `12`; crypto_alt avg `0.0239` n `228`; crypto_major avg `-0.0883` n `8`; equity avg `-0.1445` n `78`; fx avg `0.0275` n `6`; index avg `0.0187` n `23`; metal avg `-0.0181` n `18`; unknown avg `-0.4669` n `687`
- 24h: commodity avg `0.4467` n `12`; crypto_alt avg `-3.11` n `228`; crypto_major avg `-3.4112` n `8`; equity avg `1.1506` n `78`; fx avg `-0.0719` n `6`; index avg `0.2933` n `23`; metal avg `-4.1009` n `18`; unknown avg `-0.2312` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
