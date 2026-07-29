# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T10:22:46.218091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.99` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `-0.0326` n `230`; crypto_major avg `-0.0267` n `8`; equity avg `-0.1138` n `102`; fx avg `-0.0014` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0172` n `20`; unknown avg `-0.0077` n `777`
- 1h: commodity avg `0.1698` n `12`; crypto_alt avg `-0.0136` n `230`; crypto_major avg `0.0693` n `8`; equity avg `0.1068` n `102`; fx avg `-0.0257` n `6`; index avg `0.0516` n `25`; metal avg `-0.0827` n `20`; unknown avg `0.019` n `777`
- 4h: commodity avg `0.1091` n `12`; crypto_alt avg `0.2142` n `230`; crypto_major avg `0.3342` n `8`; equity avg `1.4094` n `102`; fx avg `0.031` n `6`; index avg `0.323` n `25`; metal avg `-0.0989` n `20`; unknown avg `-0.1821` n `777`
- 24h: commodity avg `0.1222` n `12`; crypto_alt avg `-1.1447` n `230`; crypto_major avg `1.3414` n `8`; equity avg `-0.4558` n `102`; fx avg `-0.0637` n `6`; index avg `-0.0123` n `25`; metal avg `0.0844` n `20`; unknown avg `-0.5291` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
