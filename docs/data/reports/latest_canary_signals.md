# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T07:37:24.512589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `0.0862` n `239`; crypto_major avg `0.038` n `8`; equity avg `0.0197` n `158`; fx avg `0.0151` n `6`; index avg `0.0176` n `27`; metal avg `0.0187` n `20`; unknown avg `0.0249` n `1264`
- 1h: commodity avg `0.045` n `13`; crypto_alt avg `0.3867` n `239`; crypto_major avg `0.2666` n `8`; equity avg `-0.0949` n `158`; fx avg `0.0176` n `6`; index avg `0.0147` n `27`; metal avg `0.0319` n `20`; unknown avg `0.0654` n `1256`
- 4h: commodity avg `0.301` n `13`; crypto_alt avg `3.0994` n `239`; crypto_major avg `2.1067` n `8`; equity avg `3.0354` n `158`; fx avg `0.0852` n `6`; index avg `0.4749` n `27`; metal avg `1.0268` n `20`; unknown avg `2.4114` n `1234`
- 24h: commodity avg `-0.2159` n `13`; crypto_alt avg `2.8366` n `239`; crypto_major avg `1.4504` n `8`; equity avg `2.3801` n `158`; fx avg `0.1679` n `6`; index avg `0.1483` n `27`; metal avg `0.8414` n `20`; unknown avg `191.7239` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2263`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
