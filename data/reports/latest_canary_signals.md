# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T06:52:26.620828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.058` n `13`; crypto_alt avg `0.1414` n `239`; crypto_major avg `0.0989` n `8`; equity avg `-0.0765` n `158`; fx avg `0.0024` n `6`; index avg `0.0074` n `27`; metal avg `0.0047` n `20`; unknown avg `0.0785` n `1264`
- 1h: commodity avg `0.1494` n `13`; crypto_alt avg `0.2394` n `239`; crypto_major avg `-0.0417` n `8`; equity avg `0.4938` n `158`; fx avg `0.0305` n `6`; index avg `0.0439` n `27`; metal avg `0.1725` n `20`; unknown avg `0.2099` n `1240`
- 4h: commodity avg `0.401` n `13`; crypto_alt avg `2.4747` n `239`; crypto_major avg `1.7695` n `8`; equity avg `2.696` n `158`; fx avg `0.0502` n `6`; index avg `0.4633` n `27`; metal avg `0.9314` n `20`; unknown avg `1.4746` n `1236`
- 24h: commodity avg `-0.1349` n `13`; crypto_alt avg `2.9908` n `239`; crypto_major avg `1.6577` n `8`; equity avg `2.4757` n `158`; fx avg `0.1687` n `6`; index avg `0.1255` n `27`; metal avg `0.7606` n `20`; unknown avg `190.5755` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2314`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
