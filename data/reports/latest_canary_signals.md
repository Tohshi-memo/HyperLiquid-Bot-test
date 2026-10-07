# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T07:37:33.150213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `13`; crypto_alt avg `0.0195` n `235`; crypto_major avg `-0.005` n `8`; equity avg `-0.0721` n `150`; fx avg `-0.0261` n `6`; index avg `-0.0059` n `26`; metal avg `-0.013` n `20`; unknown avg `0.0046` n `1076`
- 1h: commodity avg `-0.0008` n `13`; crypto_alt avg `0.1204` n `235`; crypto_major avg `-0.0092` n `8`; equity avg `-0.0723` n `150`; fx avg `-0.0702` n `6`; index avg `-0.0135` n `26`; metal avg `0.0016` n `20`; unknown avg `0.3842` n `1074`
- 4h: commodity avg `0.0995` n `13`; crypto_alt avg `0.1762` n `235`; crypto_major avg `0.3339` n `8`; equity avg `-0.1577` n `150`; fx avg `-0.0809` n `6`; index avg `-0.0563` n `26`; metal avg `-0.1318` n `20`; unknown avg `0.3369` n `1046`
- 24h: commodity avg `0.7821` n `13`; crypto_alt avg `-2.9124` n `235`; crypto_major avg `-1.737` n `8`; equity avg `-0.2885` n `149`; fx avg `-0.0478` n `6`; index avg `-0.1042` n `26`; metal avg `-0.1695` n `20`; unknown avg `814.2782` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
