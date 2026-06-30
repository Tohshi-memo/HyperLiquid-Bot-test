# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T04:22:23.905188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1115` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `0.0126` n `228`; crypto_major avg `0.0777` n `8`; equity avg `0.092` n `88`; fx avg `-0.0107` n `6`; index avg `0.0145` n `23`; metal avg `0.0464` n `20`; unknown avg `-0.1015` n `765`
- 1h: commodity avg `-0.0544` n `12`; crypto_alt avg `-0.3334` n `228`; crypto_major avg `-0.5273` n `8`; equity avg `0.2349` n `88`; fx avg `-0.0107` n `6`; index avg `0.0836` n `23`; metal avg `0.0205` n `20`; unknown avg `10.498` n `765`
- 4h: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.6635` n `228`; crypto_major avg `-0.9759` n `8`; equity avg `0.4709` n `88`; fx avg `-0.0379` n `6`; index avg `0.1356` n `23`; metal avg `-0.2732` n `20`; unknown avg `11.7537` n `763`
- 24h: commodity avg `-0.2509` n `12`; crypto_alt avg `-0.1457` n `228`; crypto_major avg `0.9635` n `8`; equity avg `2.4478` n `88`; fx avg `0.1127` n `6`; index avg `0.4271` n `23`; metal avg `-0.6256` n `20`; unknown avg `12.1821` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
