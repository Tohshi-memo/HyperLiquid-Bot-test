# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T15:22:32.291499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0476` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0105` n `233`; crypto_major avg `-0.0186` n `8`; equity avg `-0.005` n `137`; fx avg `0.015` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0038` n `20`; unknown avg `0.0594` n `909`
- 1h: commodity avg `0.1228` n `12`; crypto_alt avg `-0.53` n `233`; crypto_major avg `-0.8226` n `8`; equity avg `-0.4782` n `137`; fx avg `0.0283` n `6`; index avg `-0.0526` n `27`; metal avg `-0.0889` n `20`; unknown avg `0.2223` n `895`
- 4h: commodity avg `0.3625` n `12`; crypto_alt avg `-0.7209` n `233`; crypto_major avg `-1.2083` n `8`; equity avg `-1.0002` n `137`; fx avg `0.0579` n `6`; index avg `-0.1607` n `27`; metal avg `-0.0762` n `20`; unknown avg `1.593` n `873`
- 24h: commodity avg `0.1473` n `12`; crypto_alt avg `-1.8296` n `233`; crypto_major avg `-2.0412` n `8`; equity avg `-0.6676` n `137`; fx avg `0.2414` n `6`; index avg `-0.014` n `27`; metal avg `0.0378` n `20`; unknown avg `0.1151` n `813`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
