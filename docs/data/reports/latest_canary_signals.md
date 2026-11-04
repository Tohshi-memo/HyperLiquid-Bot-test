# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T03:07:27.336816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.24` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.3203` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1838` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.91` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0967` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0351` n `13`; crypto_alt avg `-0.7804` n `239`; crypto_major avg `-0.7628` n `8`; equity avg `-0.6213` n `158`; fx avg `-0.0116` n `6`; index avg `-0.0681` n `27`; metal avg `-0.0817` n `20`; unknown avg `0.0727` n `1258`
- 1h: commodity avg `-0.0703` n `13`; crypto_alt avg `-1.5298` n `239`; crypto_major avg `-1.38` n `8`; equity avg `-1.6988` n `158`; fx avg `0.0224` n `6`; index avg `-0.2833` n `27`; metal avg `-0.2378` n `20`; unknown avg `4.9324` n `1258`
- 4h: commodity avg `-0.4292` n `13`; crypto_alt avg `-2.5576` n `239`; crypto_major avg `-2.613` n `8`; equity avg `-3.8944` n `158`; fx avg `-0.0132` n `6`; index avg `-0.703` n `27`; metal avg `-0.2927` n `20`; unknown avg `5.0751` n `1250`
- 24h: commodity avg `-0.1475` n `13`; crypto_alt avg `-0.6327` n `239`; crypto_major avg `-1.0881` n `8`; equity avg `-1.5889` n `158`; fx avg `0.1489` n `6`; index avg `-0.4738` n `27`; metal avg `-0.5813` n `20`; unknown avg `-0.3803` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
