# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T14:22:29.809030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0633` n `13`; crypto_alt avg `-0.4407` n `235`; crypto_major avg `-0.2965` n `8`; equity avg `0.0112` n `151`; fx avg `-0.0111` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0928` n `20`; unknown avg `-0.1467` n `1134`
- 1h: commodity avg `0.1915` n `13`; crypto_alt avg `-0.5007` n `235`; crypto_major avg `-0.114` n `8`; equity avg `-1.325` n `151`; fx avg `0.0037` n `6`; index avg `-0.1177` n `26`; metal avg `-0.0721` n `20`; unknown avg `0.8283` n `1132`
- 4h: commodity avg `0.4213` n `13`; crypto_alt avg `-1.5436` n `235`; crypto_major avg `-1.0709` n `8`; equity avg `-1.589` n `151`; fx avg `0.0031` n `6`; index avg `-0.1365` n `26`; metal avg `-0.1241` n `20`; unknown avg `0.0976` n `1109`
- 24h: commodity avg `0.5791` n `13`; crypto_alt avg `-0.2945` n `235`; crypto_major avg `0.0187` n `8`; equity avg `-2.7394` n `151`; fx avg `-0.1078` n `6`; index avg `-0.2891` n `26`; metal avg `-0.1006` n `20`; unknown avg `-0.2249` n `911`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2399`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
