# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T00:07:25.849867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.6933` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.6022` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4783` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0723` n `13`; crypto_alt avg `0.0613` n `239`; crypto_major avg `-0.0074` n `8`; equity avg `-0.1431` n `158`; fx avg `-0.0333` n `6`; index avg `0.0198` n `27`; metal avg `0.0812` n `20`; unknown avg `4.1204` n `1252`
- 1h: commodity avg `-0.0818` n `13`; crypto_alt avg `-0.6059` n `239`; crypto_major avg `-0.9334` n `8`; equity avg `-0.6234` n `158`; fx avg `-0.0547` n `6`; index avg `-0.0943` n `27`; metal avg `0.0114` n `20`; unknown avg `2.9717` n `1246`
- 4h: commodity avg `-0.0189` n `13`; crypto_alt avg `-1.8851` n `239`; crypto_major avg `-2.6211` n `8`; equity avg `-1.2554` n `158`; fx avg `-0.0712` n `6`; index avg `-0.1428` n `27`; metal avg `0.0722` n `20`; unknown avg `1.1717` n `1186`
- 24h: commodity avg `-0.0928` n `13`; crypto_alt avg `-3.4999` n `239`; crypto_major avg `-3.0367` n `8`; equity avg `-1.0678` n `158`; fx avg `-0.0292` n `6`; index avg `-0.1601` n `27`; metal avg `0.0541` n `20`; unknown avg `0.4789` n `1000`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
