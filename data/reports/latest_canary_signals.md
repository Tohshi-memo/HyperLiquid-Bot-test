# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T04:52:28.961258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0285` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.2204` n `231`; crypto_major avg `0.1549` n `8`; equity avg `0.0055` n `127`; fx avg `-0.0051` n `6`; index avg `-0.0028` n `26`; metal avg `0.0145` n `20`; unknown avg `1.2166` n `792`
- 1h: commodity avg `0.0234` n `12`; crypto_alt avg `0.015` n `231`; crypto_major avg `-0.156` n `8`; equity avg `-0.0934` n `127`; fx avg `0.0069` n `6`; index avg `-0.0126` n `26`; metal avg `0.0339` n `20`; unknown avg `0.5123` n `792`
- 4h: commodity avg `0.0163` n `12`; crypto_alt avg `-1.6241` n `231`; crypto_major avg `-1.0636` n `8`; equity avg `-0.275` n `127`; fx avg `-0.0306` n `6`; index avg `-0.0351` n `26`; metal avg `0.0098` n `20`; unknown avg `0.7335` n `792`
- 24h: commodity avg `0.3225` n `12`; crypto_alt avg `0.6755` n `231`; crypto_major avg `1.828` n `8`; equity avg `-0.0325` n `127`; fx avg `-0.0358` n `6`; index avg `0.0678` n `26`; metal avg `-0.046` n `20`; unknown avg `0.5391` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
