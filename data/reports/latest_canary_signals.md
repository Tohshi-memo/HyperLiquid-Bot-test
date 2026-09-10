# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T09:52:26.092896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.1366` n `233`; crypto_major avg `-0.1004` n `8`; equity avg `0.0439` n `134`; fx avg `-0.0186` n `6`; index avg `0.0154` n `26`; metal avg `0.0337` n `20`; unknown avg `-0.194` n `797`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `-0.3208` n `233`; crypto_major avg `-0.2536` n `8`; equity avg `-0.0772` n `134`; fx avg `-0.0087` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.4123` n `795`
- 4h: commodity avg `0.2814` n `12`; crypto_alt avg `-1.0568` n `233`; crypto_major avg `-0.7866` n `8`; equity avg `-0.4153` n `134`; fx avg `0.0321` n `6`; index avg `-0.0692` n `26`; metal avg `-0.3048` n `20`; unknown avg `-0.3372` n `765`
- 24h: commodity avg `-0.0003` n `12`; crypto_alt avg `-4.3681` n `233`; crypto_major avg `-2.7995` n `8`; equity avg `-1.0237` n `134`; fx avg `0.0948` n `6`; index avg `-0.0766` n `26`; metal avg `0.1109` n `20`; unknown avg `-0.8694` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
