# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T12:37:30.446475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `13`; crypto_alt avg `-0.2243` n `239`; crypto_major avg `-0.0975` n `8`; equity avg `0.0591` n `166`; fx avg `0.001` n `6`; index avg `0.0084` n `27`; metal avg `0.1122` n `20`; unknown avg `-0.1049` n `1267`
- 1h: commodity avg `0.0358` n `13`; crypto_alt avg `-0.0178` n `239`; crypto_major avg `0.4233` n `8`; equity avg `0.1784` n `166`; fx avg `0.0212` n `6`; index avg `0.0035` n `27`; metal avg `0.1186` n `20`; unknown avg `195.7414` n `1256`
- 4h: commodity avg `0.1701` n `13`; crypto_alt avg `-1.499` n `239`; crypto_major avg `-0.409` n `8`; equity avg `-1.6162` n `166`; fx avg `0.1092` n `6`; index avg `-0.2346` n `27`; metal avg `0.1174` n `20`; unknown avg `165.2574` n `1210`
- 24h: commodity avg `-0.3452` n `13`; crypto_alt avg `-1.5148` n `239`; crypto_major avg `-1.1062` n `8`; equity avg `1.6406` n `166`; fx avg `-0.0366` n `6`; index avg `0.3466` n `27`; metal avg `-0.1764` n `20`; unknown avg `-0.3667` n `1136`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
