# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T00:37:29.926791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9695` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.845` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8288` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5442` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5357` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.4081` n `238`; crypto_major avg `0.527` n `8`; equity avg `-0.0395` n `156`; fx avg `0.0283` n `6`; index avg `-0.0111` n `27`; metal avg `0.0153` n `20`; unknown avg `0.8983` n `1260`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `-2.4099` n `238`; crypto_major avg `-1.5589` n `8`; equity avg `-0.1922` n `156`; fx avg `0.0089` n `6`; index avg `-0.0232` n `27`; metal avg `-0.0147` n `20`; unknown avg `5.5463` n `1238`
- 4h: commodity avg `-0.0144` n `13`; crypto_alt avg `-5.3755` n `238`; crypto_major avg `-2.9839` n `8`; equity avg `-1.7212` n `156`; fx avg `0.0195` n `6`; index avg `-0.1551` n `27`; metal avg `-0.1389` n `20`; unknown avg `174.6002` n `1232`
- 24h: commodity avg `-0.2209` n `13`; crypto_alt avg `-8.2281` n `238`; crypto_major avg `-3.7629` n `8`; equity avg `-3.8698` n `155`; fx avg `0.1867` n `6`; index avg `-0.3606` n `27`; metal avg `-0.5505` n `20`; unknown avg `33.4603` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
