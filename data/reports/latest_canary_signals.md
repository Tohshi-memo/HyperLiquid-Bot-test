# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T06:22:26.211738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0817` n `12`; crypto_alt avg `0.4624` n `234`; crypto_major avg `0.3986` n `8`; equity avg `0.076` n `140`; fx avg `-0.0185` n `6`; index avg `0.0063` n `26`; metal avg `-0.0155` n `20`; unknown avg `0.3317` n `944`
- 1h: commodity avg `-0.049` n `12`; crypto_alt avg `0.3876` n `234`; crypto_major avg `0.4599` n `8`; equity avg `0.1534` n `140`; fx avg `-0.0314` n `6`; index avg `0.0337` n `26`; metal avg `-0.0457` n `20`; unknown avg `1.0769` n `910`
- 4h: commodity avg `0.0176` n `12`; crypto_alt avg `1.548` n `234`; crypto_major avg `0.5177` n `8`; equity avg `0.0905` n `140`; fx avg `-0.0243` n `6`; index avg `0.0516` n `26`; metal avg `-0.0682` n `20`; unknown avg `45.4159` n `904`
- 24h: commodity avg `-0.6122` n `12`; crypto_alt avg `3.9041` n `234`; crypto_major avg `3.0463` n `8`; equity avg `1.1646` n `140`; fx avg `-0.0318` n `6`; index avg `0.2378` n `26`; metal avg `-0.0361` n `20`; unknown avg `4.4175` n `773`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
