# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T22:22:32.778506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1124` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0049` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8362` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0481` n `12`; crypto_alt avg `-0.7121` n `233`; crypto_major avg `-0.0906` n `8`; equity avg `-0.062` n `134`; fx avg `-0.0047` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0171` n `20`; unknown avg `0.0988` n `775`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-1.7259` n `233`; crypto_major avg `-0.7332` n `8`; equity avg `-0.1493` n `134`; fx avg `-0.0155` n `6`; index avg `-0.0035` n `26`; metal avg `0.0002` n `20`; unknown avg `0.663` n `735`
- 4h: commodity avg `0.104` n `12`; crypto_alt avg `-3.2588` n `233`; crypto_major avg `-2.0084` n `8`; equity avg `-0.5725` n `134`; fx avg `-0.0075` n `6`; index avg `-0.0035` n `26`; metal avg `-0.1722` n `20`; unknown avg `62.1636` n `691`
- 24h: commodity avg `0.1268` n `12`; crypto_alt avg `-3.3936` n `233`; crypto_major avg `-2.0416` n `8`; equity avg `-0.5968` n `134`; fx avg `-0.0158` n `6`; index avg `-0.1185` n `26`; metal avg `0.5501` n `20`; unknown avg `2.4` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
