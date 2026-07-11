# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T18:07:28.762919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `0.059` n `230`; crypto_major avg `-0.0673` n `8`; equity avg `-0.015` n `92`; fx avg `0.0` n `6`; index avg `0.0018` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.002` n `765`
- 1h: commodity avg `0.0415` n `12`; crypto_alt avg `0.1519` n `230`; crypto_major avg `0.0887` n `8`; equity avg `0.0473` n `92`; fx avg `0.0187` n `6`; index avg `0.0031` n `25`; metal avg `-0.0066` n `20`; unknown avg `0.189` n `765`
- 4h: commodity avg `0.0149` n `12`; crypto_alt avg `0.2609` n `230`; crypto_major avg `0.2287` n `8`; equity avg `0.178` n `92`; fx avg `-0.0149` n `6`; index avg `0.0239` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.2805` n `765`
- 24h: commodity avg `0.1367` n `12`; crypto_alt avg `1.0356` n `229`; crypto_major avg `0.6896` n `8`; equity avg `0.087` n `92`; fx avg `-0.003` n `6`; index avg `0.0236` n `25`; metal avg `0.0808` n `20`; unknown avg `2.4049` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
