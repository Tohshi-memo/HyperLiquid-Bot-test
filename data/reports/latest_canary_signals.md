# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T10:22:29.177315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.053` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.3582` n `231`; crypto_major avg `0.3012` n `8`; equity avg `0.0875` n `127`; fx avg `0.0066` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0332` n `20`; unknown avg `0.084` n `792`
- 1h: commodity avg `0.036` n `12`; crypto_alt avg `-0.3278` n `231`; crypto_major avg `-0.4424` n `8`; equity avg `0.0036` n `127`; fx avg `-0.0046` n `6`; index avg `-0.002` n `26`; metal avg `0.0504` n `20`; unknown avg `-0.0194` n `792`
- 4h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.6792` n `231`; crypto_major avg `-1.0673` n `8`; equity avg `-0.1751` n `127`; fx avg `-0.0021` n `6`; index avg `-0.0143` n `26`; metal avg `0.3747` n `20`; unknown avg `0.0291` n `792`
- 24h: commodity avg `0.2006` n `12`; crypto_alt avg `-1.1554` n `231`; crypto_major avg `-0.9774` n `8`; equity avg `-1.097` n `127`; fx avg `-0.0882` n `6`; index avg `-0.0179` n `26`; metal avg `0.7466` n `20`; unknown avg `0.2441` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
