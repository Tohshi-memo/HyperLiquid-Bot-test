# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T07:52:28.032568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `0.0148` n `234`; crypto_major avg `0.0738` n `8`; equity avg `0.0084` n `141`; fx avg `0.0025` n `6`; index avg `-0.0019` n `26`; metal avg `0.001` n `20`; unknown avg `3.3832` n `961`
- 1h: commodity avg `-0.0453` n `12`; crypto_alt avg `0.3599` n `234`; crypto_major avg `0.1631` n `8`; equity avg `0.0192` n `141`; fx avg `0.0178` n `6`; index avg `-0.005` n `26`; metal avg `-0.0057` n `20`; unknown avg `2.8292` n `959`
- 4h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.9407` n `234`; crypto_major avg `-0.0432` n `8`; equity avg `0.0503` n `141`; fx avg `0.0191` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0066` n `20`; unknown avg `2.6122` n `929`
- 24h: commodity avg `-0.0798` n `12`; crypto_alt avg `3.4903` n `234`; crypto_major avg `0.9777` n `8`; equity avg `-0.6189` n `141`; fx avg `-0.0666` n `6`; index avg `0.054` n `26`; metal avg `0.2205` n `20`; unknown avg `1125.5688` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
