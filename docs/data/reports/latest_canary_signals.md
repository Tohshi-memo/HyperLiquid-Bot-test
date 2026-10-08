# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T02:52:24.559690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `13`; crypto_alt avg `0.2125` n `235`; crypto_major avg `0.0957` n `8`; equity avg `-0.0055` n `150`; fx avg `0.0156` n `6`; index avg `0.0064` n `26`; metal avg `0.0167` n `20`; unknown avg `-0.0327` n `1077`
- 1h: commodity avg `0.1291` n `13`; crypto_alt avg `-0.0808` n `235`; crypto_major avg `-0.1095` n `8`; equity avg `-0.1223` n `150`; fx avg `0.0466` n `6`; index avg `0.0079` n `26`; metal avg `0.0506` n `20`; unknown avg `-0.4014` n `1075`
- 4h: commodity avg `0.1448` n `13`; crypto_alt avg `0.7166` n `235`; crypto_major avg `0.304` n `8`; equity avg `-0.0434` n `150`; fx avg `-0.012` n `6`; index avg `-0.0142` n `26`; metal avg `0.4201` n `20`; unknown avg `-0.0455` n `1069`
- 24h: commodity avg `0.4363` n `13`; crypto_alt avg `-0.5506` n `235`; crypto_major avg `-1.1138` n `8`; equity avg `-0.8182` n `150`; fx avg `-0.15` n `6`; index avg `-0.1665` n `26`; metal avg `-0.1484` n `20`; unknown avg `247.3178` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
