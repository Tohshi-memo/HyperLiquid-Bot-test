# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T00:52:35.714163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.0555` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8681` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7149` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.0235` n `233`; crypto_major avg `-0.0102` n `8`; equity avg `0.0671` n `136`; fx avg `-0.0196` n `6`; index avg `0.0073` n `27`; metal avg `0.06` n `20`; unknown avg `1.5574` n `908`
- 1h: commodity avg `0.0686` n `12`; crypto_alt avg `0.1602` n `233`; crypto_major avg `0.038` n `8`; equity avg `0.3258` n `136`; fx avg `0.0053` n `6`; index avg `0.0782` n `27`; metal avg `0.0016` n `20`; unknown avg `1.7053` n `900`
- 4h: commodity avg `0.1181` n `12`; crypto_alt avg `-1.2719` n `233`; crypto_major avg `-1.7748` n `8`; equity avg `0.2807` n `136`; fx avg `0.0075` n `6`; index avg `0.0933` n `27`; metal avg `-0.0599` n `20`; unknown avg `4.0278` n `888`
- 24h: commodity avg `-0.0941` n `12`; crypto_alt avg `1.0515` n `233`; crypto_major avg `1.9963` n `8`; equity avg `0.308` n `136`; fx avg `0.0413` n `6`; index avg `0.0312` n `27`; metal avg `-0.4708` n `20`; unknown avg `6.7049` n `676`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
