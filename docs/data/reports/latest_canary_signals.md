# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T22:07:31.713240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1037` n `12`; crypto_alt avg `-0.0284` n `230`; crypto_major avg `0.0236` n `8`; equity avg `0.0959` n `102`; fx avg `-0.0028` n `6`; index avg `0.0101` n `25`; metal avg `-0.0147` n `20`; unknown avg `-0.0461` n `776`
- 1h: commodity avg `0.2806` n `12`; crypto_alt avg `0.1333` n `230`; crypto_major avg `0.2651` n `8`; equity avg `0.1554` n `102`; fx avg `0.0143` n `6`; index avg `0.0555` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.1394` n `776`
- 4h: commodity avg `0.3013` n `12`; crypto_alt avg `0.2634` n `230`; crypto_major avg `0.6118` n `8`; equity avg `1.1801` n `102`; fx avg `0.0185` n `6`; index avg `0.0615` n `25`; metal avg `0.0022` n `20`; unknown avg `0.3109` n `775`
- 24h: commodity avg `-0.5453` n `12`; crypto_alt avg `-1.5314` n `230`; crypto_major avg `-0.8894` n `8`; equity avg `-2.4488` n `102`; fx avg `-0.0803` n `6`; index avg `-0.3254` n `25`; metal avg `-0.4263` n `20`; unknown avg `0.1994` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
