# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T05:22:26.892849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `13`; crypto_alt avg `-0.0682` n `239`; crypto_major avg `0.0008` n `8`; equity avg `-0.1035` n `158`; fx avg `-0.0036` n `6`; index avg `-0.0178` n `27`; metal avg `-0.0302` n `20`; unknown avg `-0.0826` n `1263`
- 1h: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.3286` n `239`; crypto_major avg `0.0839` n `8`; equity avg `-0.1952` n `158`; fx avg `-0.0185` n `6`; index avg `-0.029` n `27`; metal avg `-0.0302` n `20`; unknown avg `1.8693` n `1251`
- 4h: commodity avg `-0.1132` n `13`; crypto_alt avg `0.4197` n `239`; crypto_major avg `0.204` n `8`; equity avg `0.226` n `158`; fx avg `0.0393` n `6`; index avg `0.0109` n `27`; metal avg `0.1002` n `20`; unknown avg `-0.0031` n `1234`
- 24h: commodity avg `-2.0231` n `13`; crypto_alt avg `2.0564` n `239`; crypto_major avg `2.7591` n `8`; equity avg `-1.1982` n `158`; fx avg `0.1067` n `6`; index avg `0.0122` n `27`; metal avg `1.5898` n `20`; unknown avg `32.1445` n `1016`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2542`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
