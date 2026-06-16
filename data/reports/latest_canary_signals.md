# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T00:07:40.826423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0451` n `12`; crypto_alt avg `0.2317` n `228`; crypto_major avg `0.1436` n `8`; equity avg `-0.0557` n `77`; fx avg `0.0398` n `6`; index avg `-0.0928` n `23`; metal avg `-0.0544` n `18`; unknown avg `9.5478` n `687`
- 1h: commodity avg `0.0916` n `12`; crypto_alt avg `0.6098` n `228`; crypto_major avg `0.3109` n `8`; equity avg `-0.002` n `77`; fx avg `-0.033` n `6`; index avg `0.0169` n `23`; metal avg `-0.0914` n `18`; unknown avg `1067.091` n `687`
- 4h: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.5083` n `228`; crypto_major avg `-1.0013` n `8`; equity avg `-0.1836` n `77`; fx avg `0.0169` n `6`; index avg `-0.1212` n `23`; metal avg `-0.2422` n `18`; unknown avg `0.2444` n `679`
- 24h: commodity avg `0.6776` n `12`; crypto_alt avg `1.0945` n `228`; crypto_major avg `2.2297` n `8`; equity avg `1.4237` n `76`; fx avg `0.0674` n `6`; index avg `0.7793` n `23`; metal avg `0.0779` n `18`; unknown avg `1.6772` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
