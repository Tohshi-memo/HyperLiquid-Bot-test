# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T06:52:30.921010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `0.0764` n `234`; crypto_major avg `0.0809` n `8`; equity avg `0.0224` n `141`; fx avg `0.014` n `6`; index avg `0.0005` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.0231` n `961`
- 1h: commodity avg `0.0` n `12`; crypto_alt avg `0.3269` n `234`; crypto_major avg `-0.036` n `8`; equity avg `-0.0059` n `141`; fx avg `0.0057` n `6`; index avg `0.0023` n `26`; metal avg `0.0049` n `20`; unknown avg `-0.2046` n `935`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.369` n `234`; crypto_major avg `-0.528` n `8`; equity avg `-0.0155` n `141`; fx avg `0.0214` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.3228` n `929`
- 24h: commodity avg `0.1352` n `12`; crypto_alt avg `3.4932` n `234`; crypto_major avg `0.8973` n `8`; equity avg `-0.6609` n `141`; fx avg `-0.0888` n `6`; index avg `0.0571` n `26`; metal avg `0.1872` n `20`; unknown avg `1129.3672` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
