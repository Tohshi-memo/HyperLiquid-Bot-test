# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T01:22:39.542744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `12`; crypto_alt avg `0.0967` n `228`; crypto_major avg `0.1035` n `8`; equity avg `0.283` n `86`; fx avg `-0.0011` n `6`; index avg `0.0788` n `23`; metal avg `0.0789` n `20`; unknown avg `39.1622` n `765`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.4152` n `228`; crypto_major avg `-0.565` n `8`; equity avg `-0.2276` n `86`; fx avg `0.0117` n `6`; index avg `-0.0025` n `23`; metal avg `0.032` n `20`; unknown avg `-0.2162` n `765`
- 4h: commodity avg `0.064` n `12`; crypto_alt avg `0.3224` n `228`; crypto_major avg `0.3828` n `8`; equity avg `-0.6102` n `86`; fx avg `0.0381` n `6`; index avg `-0.0928` n `23`; metal avg `-0.0855` n `20`; unknown avg `0.2193` n `749`
- 24h: commodity avg `0.4268` n `12`; crypto_alt avg `-1.233` n `228`; crypto_major avg `-1.5538` n `8`; equity avg `-2.4445` n `86`; fx avg `0.0542` n `6`; index avg `-0.1661` n `23`; metal avg `0.3095` n `20`; unknown avg `0.4738` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
