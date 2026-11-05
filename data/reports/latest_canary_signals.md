# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T11:52:31.706210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0958` n `13`; crypto_alt avg `-0.1136` n `239`; crypto_major avg `0.033` n `8`; equity avg `-0.0448` n `158`; fx avg `0.0046` n `6`; index avg `-0.017` n `27`; metal avg `-0.0278` n `20`; unknown avg `0.0306` n `1255`
- 1h: commodity avg `0.188` n `13`; crypto_alt avg `-0.0257` n `239`; crypto_major avg `0.033` n `8`; equity avg `-0.1045` n `158`; fx avg `-0.0116` n `6`; index avg `-0.0007` n `27`; metal avg `0.061` n `20`; unknown avg `15.0346` n `1251`
- 4h: commodity avg `0.3598` n `13`; crypto_alt avg `-0.0051` n `239`; crypto_major avg `0.1437` n `8`; equity avg `0.0235` n `158`; fx avg `-0.0097` n `6`; index avg `0.0108` n `27`; metal avg `0.1157` n `20`; unknown avg `18.2112` n `1135`
- 24h: commodity avg `-1.0729` n `13`; crypto_alt avg `0.0136` n `239`; crypto_major avg `1.2099` n `8`; equity avg `-3.166` n `158`; fx avg `-0.0488` n `6`; index avg `-0.3077` n `27`; metal avg `0.6923` n `20`; unknown avg `18.5269` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.204`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
