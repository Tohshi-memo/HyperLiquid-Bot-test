# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T20:55:36.180352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1652` n `12`; crypto_alt avg `0.1919` n `228`; crypto_major avg `0.0263` n `8`; equity avg `0.1259` n `66`; fx avg `-0.0014` n `6`; index avg `-0.0661` n `23`; metal avg `-0.0307` n `18`; unknown avg `0.0305` n `384`
- 1h: commodity avg `0.1826` n `12`; crypto_alt avg `-0.0082` n `228`; crypto_major avg `-0.1979` n `8`; equity avg `0.0393` n `66`; fx avg `-0.0665` n `6`; index avg `-0.0935` n `23`; metal avg `-0.1688` n `18`; unknown avg `-0.1614` n `384`
- 4h: commodity avg `0.4083` n `12`; crypto_alt avg `0.3479` n `228`; crypto_major avg `0.0753` n `8`; equity avg `0.237` n `66`; fx avg `-0.0419` n `6`; index avg `0.124` n `23`; metal avg `0.1188` n `18`; unknown avg `0.2635` n `384`
- 24h: commodity avg `-2.3162` n `12`; crypto_alt avg `2.779` n `228`; crypto_major avg `1.7956` n `8`; equity avg `1.727` n `66`; fx avg `-0.0828` n `6`; index avg `1.1606` n `23`; metal avg `1.5832` n `18`; unknown avg `0.8612` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
