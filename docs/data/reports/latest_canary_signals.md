# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T22:07:26.399484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1051` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9653` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8256` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.064` n `12`; crypto_alt avg `-0.339` n `233`; crypto_major avg `-0.3727` n `8`; equity avg `-0.0216` n `134`; fx avg `-0.0089` n `6`; index avg `0.0073` n `26`; metal avg `0.0284` n `20`; unknown avg `0.3221` n `743`
- 1h: commodity avg `0.0725` n `12`; crypto_alt avg `-1.266` n `233`; crypto_major avg `-0.8841` n `8`; equity avg `-0.1716` n `134`; fx avg `-0.002` n `6`; index avg `-0.0046` n `26`; metal avg `0.008` n `20`; unknown avg `1.6352` n `735`
- 4h: commodity avg `0.1333` n `12`; crypto_alt avg `-2.6005` n `233`; crypto_major avg `-1.9718` n `8`; equity avg `-0.5389` n `134`; fx avg `-0.0096` n `6`; index avg `-0.0065` n `26`; metal avg `-0.1462` n `20`; unknown avg `62.9165` n `691`
- 24h: commodity avg `0.155` n `12`; crypto_alt avg `-2.6937` n `233`; crypto_major avg `-1.8849` n `8`; equity avg `-0.562` n `134`; fx avg `-0.0145` n `6`; index avg `-0.1224` n `26`; metal avg `0.5502` n `20`; unknown avg `3.2046` n `641`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
