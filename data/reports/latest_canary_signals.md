# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T16:37:31.906442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.0512` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.0497` n `237`; crypto_major avg `-0.0803` n `8`; equity avg `-0.3514` n `151`; fx avg `-0.0022` n `6`; index avg `-0.064` n `26`; metal avg `-0.046` n `20`; unknown avg `-0.3839` n `1233`
- 1h: commodity avg `0.0982` n `13`; crypto_alt avg `-0.1148` n `237`; crypto_major avg `-0.0504` n `8`; equity avg `-0.1567` n `151`; fx avg `0.0273` n `6`; index avg `-0.003` n `26`; metal avg `-0.1057` n `20`; unknown avg `0.3984` n `1225`
- 4h: commodity avg `-0.0729` n `13`; crypto_alt avg `-0.9355` n `237`; crypto_major avg `-0.1894` n `8`; equity avg `-2.2406` n `151`; fx avg `0.0563` n `6`; index avg `-0.1601` n `26`; metal avg `-0.2621` n `20`; unknown avg `-0.079` n `1083`
- 24h: commodity avg `0.4128` n `13`; crypto_alt avg `-4.8187` n `237`; crypto_major avg `-3.4333` n `8`; equity avg `-4.6174` n `151`; fx avg `-0.138` n `6`; index avg `-0.5726` n `26`; metal avg `-0.9533` n `20`; unknown avg `2.5784` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
