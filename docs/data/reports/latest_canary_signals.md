# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T16:22:27.092616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9415` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.61` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.283` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2545` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0457` n `13`; crypto_alt avg `0.0357` n `239`; crypto_major avg `-0.2266` n `8`; equity avg `0.1022` n `166`; fx avg `-0.0461` n `6`; index avg `0.0231` n `27`; metal avg `0.0589` n `20`; unknown avg `2.484` n `1264`
- 1h: commodity avg `-0.0841` n `13`; crypto_alt avg `-0.5793` n `239`; crypto_major avg `-1.3087` n `8`; equity avg `-0.5044` n `166`; fx avg `-0.057` n `6`; index avg `-0.0542` n `27`; metal avg `-0.0872` n `20`; unknown avg `196.2046` n `1256`
- 4h: commodity avg `-0.772` n `13`; crypto_alt avg `2.7251` n `239`; crypto_major avg `3.1695` n `8`; equity avg `5.4525` n `166`; fx avg `-0.2129` n `6`; index avg `0.6189` n `27`; metal avg `0.5595` n `20`; unknown avg `328.8271` n `1252`
- 24h: commodity avg `-1.6221` n `13`; crypto_alt avg `3.1833` n `239`; crypto_major avg `3.7074` n `8`; equity avg `6.9285` n `166`; fx avg `-0.0643` n `6`; index avg `0.6448` n `27`; metal avg `0.8231` n `20`; unknown avg `245.9619` n `1059`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
