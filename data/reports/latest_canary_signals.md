# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T03:22:24.842878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.1112` n `230`; crypto_major avg `-0.0679` n `8`; equity avg `-0.4423` n `102`; fx avg `-0.0198` n `6`; index avg `-0.081` n `25`; metal avg `-0.0997` n `20`; unknown avg `-0.0409` n `779`
- 1h: commodity avg `-0.0374` n `12`; crypto_alt avg `-0.2206` n `230`; crypto_major avg `-0.2748` n `8`; equity avg `-1.1486` n `102`; fx avg `-0.0132` n `6`; index avg `-0.2193` n `25`; metal avg `-0.2341` n `20`; unknown avg `-0.0019` n `779`
- 4h: commodity avg `-0.1891` n `12`; crypto_alt avg `0.535` n `230`; crypto_major avg `0.2568` n `8`; equity avg `-0.053` n `102`; fx avg `-0.035` n `6`; index avg `-0.0103` n `25`; metal avg `-0.3039` n `20`; unknown avg `-0.0373` n `778`
- 24h: commodity avg `0.3882` n `12`; crypto_alt avg `-0.6809` n `230`; crypto_major avg `0.063` n `8`; equity avg `-2.3174` n `102`; fx avg `0.0226` n `6`; index avg `-0.1502` n `25`; metal avg `0.1009` n `20`; unknown avg `-0.6079` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
