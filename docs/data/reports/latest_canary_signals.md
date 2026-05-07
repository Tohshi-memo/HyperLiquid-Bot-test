# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T02:37:12.797684+00:00`
- Correlation status: `ready`
- Asset price records: `510`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0567` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0291` n `12`; crypto_alt avg `0.1028` n `228`; crypto_major avg `0.04` n `8`; equity avg `0.0762` n `65`; fx avg `-0.0121` n `4`; index avg `-0.0066` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.0097` n `358`
- 1h: commodity avg `-0.1038` n `12`; crypto_alt avg `-0.3202` n `228`; crypto_major avg `-0.3658` n `8`; equity avg `0.1985` n `65`; fx avg `-0.0002` n `4`; index avg `0.0412` n `23`; metal avg `-0.1191` n `18`; unknown avg `-0.4789` n `358`
- 4h: commodity avg `-0.2386` n `12`; crypto_alt avg `-0.9908` n `228`; crypto_major avg `-0.8948` n `8`; equity avg `0.099` n `65`; fx avg `0.067` n `4`; index avg `0.1619` n `23`; metal avg `0.1605` n `18`; unknown avg `-0.4653` n `356`
- 24h: commodity avg `-1.7716` n `7`; crypto_alt avg `0.4401` n `223`; crypto_major avg `-0.7801` n `7`; equity avg `1.6451` n `47`; fx avg `-0.2832` n `4`; index avg `1.1209` n `6`; metal avg `2.1502` n `7`; unknown avg `2.4726` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1381`, n `506`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1222`, n `506`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `506`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `506`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0777`, n `502`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `502`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0706`, n `502`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `502`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `506`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0678`, n `502`, weak_sample_signal
