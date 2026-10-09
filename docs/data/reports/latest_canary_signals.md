# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T10:52:27.022456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0399` n `13`; crypto_alt avg `-0.2086` n `235`; crypto_major avg `-0.2257` n `8`; equity avg `-0.0189` n `150`; fx avg `-0.0057` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.9394` n `1078`
- 1h: commodity avg `0.0372` n `13`; crypto_alt avg `-0.7826` n `235`; crypto_major avg `-0.548` n `8`; equity avg `-0.0946` n `150`; fx avg `-0.0148` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0424` n `20`; unknown avg `1.2215` n `1076`
- 4h: commodity avg `-0.0831` n `13`; crypto_alt avg `-0.9377` n `235`; crypto_major avg `-0.5661` n `8`; equity avg `-0.0584` n `150`; fx avg `-0.0171` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0504` n `20`; unknown avg `-0.3883` n `1006`
- 24h: commodity avg `-0.57` n `13`; crypto_alt avg `-1.8976` n `235`; crypto_major avg `-2.035` n `8`; equity avg `-0.2085` n `150`; fx avg `0.0419` n `6`; index avg `0.0878` n `26`; metal avg `0.4571` n `20`; unknown avg `7.3709` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
