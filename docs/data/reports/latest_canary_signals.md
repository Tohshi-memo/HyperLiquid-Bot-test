# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T22:07:31.463455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0416` n `13`; crypto_alt avg `-0.239` n `235`; crypto_major avg `-0.1273` n `8`; equity avg `-0.0388` n `151`; fx avg `0.0009` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0203` n `20`; unknown avg `0.0709` n `1077`
- 1h: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.1087` n `235`; crypto_major avg `-0.0622` n `8`; equity avg `0.0233` n `151`; fx avg `0.0063` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0032` n `20`; unknown avg `1.5184` n `1077`
- 4h: commodity avg `0.138` n `13`; crypto_alt avg `0.1936` n `235`; crypto_major avg `-0.0071` n `8`; equity avg `0.3046` n `151`; fx avg `-0.0068` n `6`; index avg `0.0147` n `26`; metal avg `-0.0042` n `20`; unknown avg `1.5496` n `1019`
- 24h: commodity avg `0.7735` n `13`; crypto_alt avg `-0.6014` n `235`; crypto_major avg `0.0317` n `8`; equity avg `-0.5886` n `151`; fx avg `0.1532` n `6`; index avg `-0.1708` n `26`; metal avg `-0.3046` n `20`; unknown avg `0.8811` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1575`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1432`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0913`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0818`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
