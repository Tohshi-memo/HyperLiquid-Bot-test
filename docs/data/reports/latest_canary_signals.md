# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T12:22:17.826044+00:00`
- Correlation status: `ready`
- Asset price records: `453`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6272` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.246` n `7`; crypto_alt avg `0.1676` n `223`; crypto_major avg `0.1423` n `7`; equity avg `-0.1583` n `47`; fx avg `0.0169` n `4`; index avg `-0.2626` n `6`; metal avg `0.0104` n `7`; unknown avg `0.0478` n `313`
- 1h: commodity avg `1.361` n `7`; crypto_alt avg `-0.206` n `223`; crypto_major avg `-0.1285` n `7`; equity avg `-0.7379` n `47`; fx avg `0.0859` n `4`; index avg `-0.3455` n `6`; metal avg `-0.6349` n `7`; unknown avg `-0.1351` n `313`
- 4h: commodity avg `-1.3462` n `7`; crypto_alt avg `0.9312` n `223`; crypto_major avg `1.281` n `7`; equity avg `0.5588` n `47`; fx avg `-0.0548` n `4`; index avg `0.9151` n `6`; metal avg `0.4549` n `7`; unknown avg `0.0186` n `313`
- 24h: commodity avg `-2.9228` n `7`; crypto_alt avg `3.6565` n `223`; crypto_major avg `2.8859` n `7`; equity avg `2.885` n `47`; fx avg `-0.5817` n `4`; index avg `2.7523` n `6`; metal avg `2.0321` n `7`; unknown avg `1.8559` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1652`, n `449`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1593`, n `449`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1445`, n `449`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `449`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `449`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.116`, n `449`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `445`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `445`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `445`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `445`, weak_sample_signal
