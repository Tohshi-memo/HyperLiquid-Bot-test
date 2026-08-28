# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T12:22:26.744688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `-0.0259` n `231`; crypto_major avg `-0.0362` n `8`; equity avg `0.0973` n `127`; fx avg `-0.0072` n `6`; index avg `0.0172` n `26`; metal avg `0.0266` n `20`; unknown avg `0.053` n `792`
- 1h: commodity avg `-0.1897` n `12`; crypto_alt avg `-0.2543` n `231`; crypto_major avg `-0.3309` n `8`; equity avg `-0.0769` n `127`; fx avg `-0.0205` n `6`; index avg `0.01` n `26`; metal avg `0.0704` n `20`; unknown avg `0.2174` n `792`
- 4h: commodity avg `-0.1806` n `12`; crypto_alt avg `0.0131` n `231`; crypto_major avg `-0.513` n `8`; equity avg `0.0372` n `127`; fx avg `0.031` n `6`; index avg `0.0255` n `26`; metal avg `0.1771` n `20`; unknown avg `0.1683` n `792`
- 24h: commodity avg `-0.1021` n `12`; crypto_alt avg `-0.3889` n `231`; crypto_major avg `-0.0552` n `8`; equity avg `-0.8719` n `127`; fx avg `-0.0368` n `6`; index avg `-0.0121` n `26`; metal avg `0.759` n `20`; unknown avg `0.507` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
