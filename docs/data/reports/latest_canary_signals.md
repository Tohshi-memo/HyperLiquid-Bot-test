# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T19:23:51.924840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `12`; crypto_alt avg `0.1044` n `233`; crypto_major avg `-0.0473` n `8`; equity avg `-0.1421` n `134`; fx avg `0.0067` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0397` n `20`; unknown avg `1.4341` n `797`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.6434` n `233`; crypto_major avg `-0.5446` n `8`; equity avg `-0.3627` n `134`; fx avg `-0.0404` n `6`; index avg `-0.0697` n `26`; metal avg `-0.1613` n `20`; unknown avg `0.6986` n `795`
- 4h: commodity avg `0.1423` n `12`; crypto_alt avg `-0.6564` n `232`; crypto_major avg `0.2006` n `8`; equity avg `-0.1828` n `134`; fx avg `-0.0626` n `6`; index avg `-0.0558` n `26`; metal avg `-0.2033` n `20`; unknown avg `0.3124` n `765`
- 24h: commodity avg `0.0057` n `12`; crypto_alt avg `0.0124` n `232`; crypto_major avg `0.0662` n `8`; equity avg `0.608` n `134`; fx avg `-0.0938` n `6`; index avg `-0.1127` n `26`; metal avg `-0.2173` n `20`; unknown avg `3.5167` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
