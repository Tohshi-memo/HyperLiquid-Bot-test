# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T05:52:23.523693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0596` n `12`; crypto_alt avg `0.0277` n `231`; crypto_major avg `0.0247` n `8`; equity avg `-0.0123` n `127`; fx avg `-0.0068` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0172` n `20`; unknown avg `-0.0478` n `792`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.0455` n `231`; crypto_major avg `0.1637` n `8`; equity avg `-0.3071` n `127`; fx avg `-0.0172` n `6`; index avg `-0.0524` n `26`; metal avg `-0.0318` n `20`; unknown avg `0.2594` n `792`
- 4h: commodity avg `0.059` n `12`; crypto_alt avg `-1.6451` n `231`; crypto_major avg `-0.9796` n `8`; equity avg `-0.5814` n `127`; fx avg `-0.0226` n `6`; index avg `-0.0613` n `26`; metal avg `0.0572` n `20`; unknown avg `0.469` n `792`
- 24h: commodity avg `0.3719` n `12`; crypto_alt avg `0.5079` n `231`; crypto_major avg `1.3574` n `8`; equity avg `-0.2615` n `127`; fx avg `-0.0597` n `6`; index avg `0.047` n `26`; metal avg `0.0861` n `20`; unknown avg `0.5086` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.079`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0608`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0532`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0509`, n `669`, weak_sample_signal
