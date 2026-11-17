# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T18:37:36.330883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.456` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0492` n `13`; crypto_alt avg `0.2695` n `239`; crypto_major avg `0.149` n `8`; equity avg `0.2635` n `163`; fx avg `-0.0101` n `6`; index avg `0.0218` n `27`; metal avg `0.0338` n `20`; unknown avg `0.5156` n `1265`
- 1h: commodity avg `0.1916` n `13`; crypto_alt avg `0.0271` n `239`; crypto_major avg `0.2295` n `8`; equity avg `0.0223` n `163`; fx avg `-0.0059` n `6`; index avg `-0.0015` n `27`; metal avg `-0.0133` n `20`; unknown avg `0.1046` n `1263`
- 4h: commodity avg `0.153` n `13`; crypto_alt avg `-1.443` n `239`; crypto_major avg `-1.5512` n `8`; equity avg `-1.3049` n `163`; fx avg `0.0452` n `6`; index avg `-0.0952` n `27`; metal avg `-0.1112` n `20`; unknown avg `2.5527` n `1245`
- 24h: commodity avg `0.1997` n `13`; crypto_alt avg `-0.4533` n `239`; crypto_major avg `-0.0299` n `8`; equity avg `-1.5447` n `163`; fx avg `0.0456` n `6`; index avg `-0.2098` n `27`; metal avg `0.112` n `20`; unknown avg `8.2081` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
