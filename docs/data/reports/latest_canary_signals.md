# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T18:22:22.709941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3796` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1395` n `12`; crypto_alt avg `0.1365` n `228`; crypto_major avg `0.1432` n `8`; equity avg `-0.0847` n `74`; fx avg `0.0021` n `6`; index avg `-0.027` n `23`; metal avg `0.0628` n `18`; unknown avg `-0.1651` n `424`
- 1h: commodity avg `-0.1453` n `12`; crypto_alt avg `-0.4486` n `228`; crypto_major avg `-0.1657` n `8`; equity avg `0.0956` n `74`; fx avg `-0.0081` n `6`; index avg `0.1303` n `23`; metal avg `0.1778` n `18`; unknown avg `-0.5162` n `424`
- 4h: commodity avg `-0.1901` n `12`; crypto_alt avg `-0.1876` n `228`; crypto_major avg `-0.6187` n `8`; equity avg `0.6654` n `74`; fx avg `-0.0471` n `6`; index avg `0.7609` n `23`; metal avg `0.1698` n `18`; unknown avg `1.2342` n `424`
- 24h: commodity avg `-0.9607` n `12`; crypto_alt avg `-5.2841` n `228`; crypto_major avg `-3.9878` n `8`; equity avg `-1.1835` n `73`; fx avg `0.0838` n `6`; index avg `0.0184` n `23`; metal avg `0.8342` n `18`; unknown avg `0.2971` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
