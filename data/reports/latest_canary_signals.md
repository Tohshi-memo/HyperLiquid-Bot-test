# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T11:07:30.046509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `0.1286` n `234`; crypto_major avg `0.1808` n `8`; equity avg `0.0022` n `140`; fx avg `-0.0121` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0142` n `20`; unknown avg `0.6878` n `940`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `0.4509` n `234`; crypto_major avg `0.2886` n `8`; equity avg `-0.0065` n `140`; fx avg `-0.0086` n `6`; index avg `-0.014` n `26`; metal avg `0.0079` n `20`; unknown avg `0.5924` n `940`
- 4h: commodity avg `0.0085` n `12`; crypto_alt avg `1.3297` n `234`; crypto_major avg `0.2286` n `8`; equity avg `0.02` n `140`; fx avg `-0.0065` n `6`; index avg `0.0017` n `26`; metal avg `0.0037` n `20`; unknown avg `1.0683` n `934`
- 24h: commodity avg `0.1786` n `12`; crypto_alt avg `4.4126` n `234`; crypto_major avg `3.9938` n `8`; equity avg `0.373` n `140`; fx avg `-0.0167` n `6`; index avg `-0.0194` n `26`; metal avg `-0.2008` n `20`; unknown avg `2.7859` n `803`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
