# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T04:07:25.270483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `13`; crypto_alt avg `-0.1917` n `239`; crypto_major avg `-0.1872` n `8`; equity avg `-0.067` n `163`; fx avg `0.0041` n `6`; index avg `-0.0068` n `27`; metal avg `-0.0884` n `20`; unknown avg `0.2797` n `1252`
- 1h: commodity avg `-0.0931` n `13`; crypto_alt avg `0.1359` n `239`; crypto_major avg `-0.0453` n `8`; equity avg `0.1542` n `163`; fx avg `0.0048` n `6`; index avg `0.0385` n `27`; metal avg `-0.0835` n `20`; unknown avg `3.5556` n `1256`
- 4h: commodity avg `-0.2778` n `13`; crypto_alt avg `-0.8802` n `239`; crypto_major avg `-0.8552` n `8`; equity avg `-1.5638` n `163`; fx avg `-0.0244` n `6`; index avg `-0.1708` n `27`; metal avg `-0.5922` n `20`; unknown avg `5.4183` n `1256`
- 24h: commodity avg `0.2583` n `13`; crypto_alt avg `-0.2038` n `239`; crypto_major avg `-0.0371` n `8`; equity avg `-0.3294` n `163`; fx avg `-0.1009` n `6`; index avg `-0.0195` n `27`; metal avg `-0.808` n `20`; unknown avg `7.3419` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
