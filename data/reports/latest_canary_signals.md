# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T23:52:24.681414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.0413` n `230`; crypto_major avg `-0.0374` n `8`; equity avg `-0.0998` n `108`; fx avg `-0.0041` n `6`; index avg `-0.0447` n `25`; metal avg `0.0565` n `20`; unknown avg `-0.0161` n `782`
- 1h: commodity avg `-0.0226` n `12`; crypto_alt avg `0.0492` n `230`; crypto_major avg `0.0375` n `8`; equity avg `-0.2364` n `108`; fx avg `-0.002` n `6`; index avg `-0.0808` n `25`; metal avg `0.1414` n `20`; unknown avg `0.2958` n `782`
- 4h: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0948` n `230`; crypto_major avg `-0.5638` n `8`; equity avg `-0.8314` n `108`; fx avg `0.0057` n `6`; index avg `-0.1105` n `25`; metal avg `0.146` n `20`; unknown avg `0.3479` n `782`
- 24h: commodity avg `-0.0319` n `12`; crypto_alt avg `0.6118` n `230`; crypto_major avg `0.6847` n `8`; equity avg `-1.1374` n `108`; fx avg `-0.0423` n `6`; index avg `-0.1712` n `25`; metal avg `0.9825` n `20`; unknown avg `1.2602` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
