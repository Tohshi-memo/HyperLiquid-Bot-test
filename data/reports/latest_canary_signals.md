# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T15:52:30.406101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-5.5569` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-5.0319` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `4.5568` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-3.1994` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.9372` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.7393` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `2.7208` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0412` n `13`; crypto_alt avg `-1.8103` n `239`; crypto_major avg `-1.3898` n `8`; equity avg `-2.6707` n `158`; fx avg `0.0236` n `6`; index avg `-0.2292` n `27`; metal avg `-0.1475` n `20`; unknown avg `45.2519` n `1256`
- 1h: commodity avg `0.0667` n `13`; crypto_alt avg `-4.0107` n `239`; crypto_major avg `-3.1327` n `8`; equity avg `-4.024` n `158`; fx avg `0.059` n `6`; index avg `-0.4119` n `27`; metal avg `-0.1955` n `20`; unknown avg `38.1275` n `1252`
- 4h: commodity avg `0.2286` n `13`; crypto_alt avg `-5.9906` n `239`; crypto_major avg `-5.3283` n `8`; equity avg `-8.0676` n `158`; fx avg `0.1171` n `6`; index avg `-0.7715` n `27`; metal avg `-0.2964` n `20`; unknown avg `68.0785` n `1243`
- 24h: commodity avg `-0.5273` n `13`; crypto_alt avg `-7.1756` n `239`; crypto_major avg `-5.8722` n `8`; equity avg `-8.9298` n `158`; fx avg `0.0994` n `6`; index avg `-0.9844` n `27`; metal avg `0.3263` n `20`; unknown avg `213.4076` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2393`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
