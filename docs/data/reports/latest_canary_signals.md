# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T15:52:49.181089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3034` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.1761` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.155` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `-2.0784` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.9858` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.8557` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0859` n `13`; crypto_alt avg `-1.6696` n `239`; crypto_major avg `-1.9016` n `8`; equity avg `-1.5965` n `163`; fx avg `0.0212` n `6`; index avg `-0.175` n `27`; metal avg `-0.0729` n `20`; unknown avg `2.1478` n `1253`
- 1h: commodity avg `-0.0689` n `13`; crypto_alt avg `-2.0721` n `239`; crypto_major avg `-2.245` n `8`; equity avg `-2.6034` n `163`; fx avg `0.0257` n `6`; index avg `-0.2592` n `27`; metal avg `-0.09` n `20`; unknown avg `2.7909` n `1251`
- 4h: commodity avg `0.0673` n `13`; crypto_alt avg `-2.1569` n `239`; crypto_major avg `-2.2361` n `8`; equity avg `-3.5377` n `163`; fx avg `0.0483` n `6`; index avg `-0.3804` n `27`; metal avg `-0.1577` n `20`; unknown avg `4.9024` n `1205`
- 24h: commodity avg `-0.275` n `13`; crypto_alt avg `-0.9983` n `239`; crypto_major avg `-0.9981` n `8`; equity avg `-4.0466` n `163`; fx avg `0.0062` n `6`; index avg `-0.4866` n `27`; metal avg `-0.0421` n `20`; unknown avg `7.9496` n `1092`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
