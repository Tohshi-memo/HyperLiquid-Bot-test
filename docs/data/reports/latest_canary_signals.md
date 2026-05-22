# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T17:52:17.503580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1918` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1494` n `12`; crypto_alt avg `-0.2729` n `228`; crypto_major avg `-0.2022` n `8`; equity avg `-0.1904` n `67`; fx avg `0.0019` n `6`; index avg `-0.0554` n `23`; metal avg `0.009` n `18`; unknown avg `0.346` n `386`
- 1h: commodity avg `-0.298` n `12`; crypto_alt avg `-0.0269` n `228`; crypto_major avg `-0.0602` n `8`; equity avg `-0.0064` n `67`; fx avg `-0.0013` n `6`; index avg `0.0881` n `23`; metal avg `0.1691` n `18`; unknown avg `0.4034` n `386`
- 4h: commodity avg `-1.0365` n `12`; crypto_alt avg `-0.8987` n `228`; crypto_major avg `-1.0976` n `8`; equity avg `-0.3528` n `67`; fx avg `0.0548` n `6`; index avg `0.0942` n `23`; metal avg `0.073` n `18`; unknown avg `-0.4566` n `386`
- 24h: commodity avg `-0.6976` n `12`; crypto_alt avg `-0.4463` n `228`; crypto_major avg `-1.1794` n `8`; equity avg `-0.3519` n `67`; fx avg `0.1748` n `6`; index avg `0.6595` n `23`; metal avg `-1.0045` n `18`; unknown avg `-0.997` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0442`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0416`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0398`, n `668`, weak_sample_signal
