# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T07:37:32.075501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0954` n `12`; crypto_alt avg `-0.1975` n `230`; crypto_major avg `-0.1208` n `8`; equity avg `-0.0852` n `102`; fx avg `0.0121` n `6`; index avg `-0.0657` n `25`; metal avg `-0.0592` n `20`; unknown avg `-0.0576` n `779`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.0815` n `230`; crypto_major avg `0.0653` n `8`; equity avg `-0.3209` n `102`; fx avg `0.0123` n `6`; index avg `-0.1057` n `25`; metal avg `0.0446` n `20`; unknown avg `1.963` n `779`
- 4h: commodity avg `0.4113` n `12`; crypto_alt avg `-0.1169` n `230`; crypto_major avg `-0.125` n `8`; equity avg `-0.3714` n `102`; fx avg `-0.0689` n `6`; index avg `-0.1718` n `25`; metal avg `-0.0847` n `20`; unknown avg `2.203` n `747`
- 24h: commodity avg `0.9478` n `12`; crypto_alt avg `-0.4631` n `230`; crypto_major avg `-0.7494` n `8`; equity avg `-3.4963` n `102`; fx avg `-0.004` n `6`; index avg `-0.5972` n `25`; metal avg `-0.1882` n `20`; unknown avg `-0.7706` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
