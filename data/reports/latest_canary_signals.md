# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T08:52:30.721611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0573` n `13`; crypto_alt avg `0.0425` n `236`; crypto_major avg `-0.025` n `8`; equity avg `0.1696` n `151`; fx avg `0.0178` n `6`; index avg `0.0167` n `26`; metal avg `-0.0522` n `20`; unknown avg `-0.0054` n `1136`
- 1h: commodity avg `0.1342` n `13`; crypto_alt avg `0.6259` n `236`; crypto_major avg `0.1742` n `8`; equity avg `-0.0622` n `151`; fx avg `0.0497` n `6`; index avg `-0.0063` n `26`; metal avg `0.0422` n `20`; unknown avg `0.1165` n `1118`
- 4h: commodity avg `0.059` n `13`; crypto_alt avg `-0.422` n `236`; crypto_major avg `-0.3207` n `8`; equity avg `-0.7751` n `151`; fx avg `-0.0159` n `6`; index avg `-0.0601` n `26`; metal avg `0.1123` n `20`; unknown avg `5.6251` n `1092`
- 24h: commodity avg `-0.2986` n `13`; crypto_alt avg `-4.5617` n `236`; crypto_major avg `-3.1355` n `8`; equity avg `-5.8475` n `151`; fx avg `0.0973` n `6`; index avg `-0.9412` n `26`; metal avg `-0.4678` n `20`; unknown avg `2.3793` n `938`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1154`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0895`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0767`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0699`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
