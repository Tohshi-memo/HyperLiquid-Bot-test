# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T13:37:27.236491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `13`; crypto_alt avg `0.0185` n `239`; crypto_major avg `-0.1916` n `8`; equity avg `-0.0995` n `161`; fx avg `0.0028` n `6`; index avg `-0.0171` n `27`; metal avg `-0.0182` n `20`; unknown avg `19.6436` n `1261`
- 1h: commodity avg `-0.0072` n `13`; crypto_alt avg `0.129` n `239`; crypto_major avg `0.01` n `8`; equity avg `-0.1337` n `161`; fx avg `-0.0373` n `6`; index avg `-0.0204` n `27`; metal avg `0.0098` n `20`; unknown avg `0.8801` n `1255`
- 4h: commodity avg `0.2099` n `13`; crypto_alt avg `0.8807` n `239`; crypto_major avg `0.446` n `8`; equity avg `0.6309` n `161`; fx avg `0.0353` n `6`; index avg `0.0384` n `27`; metal avg `0.0007` n `20`; unknown avg `1.0571` n `1247`
- 24h: commodity avg `1.1234` n `13`; crypto_alt avg `-0.2061` n `239`; crypto_major avg `-0.8244` n `8`; equity avg `4.3874` n `161`; fx avg `-0.2154` n `6`; index avg `0.3744` n `27`; metal avg `0.3092` n `20`; unknown avg `2.0822` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2973`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
