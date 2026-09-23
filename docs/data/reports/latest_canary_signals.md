# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T00:52:33.583135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.0679` n `234`; crypto_major avg `0.0604` n `8`; equity avg `-0.0485` n `140`; fx avg `0.0124` n `6`; index avg `-0.0237` n `26`; metal avg `0.0071` n `20`; unknown avg `-0.1576` n `945`
- 1h: commodity avg `0.071` n `12`; crypto_alt avg `-0.1004` n `234`; crypto_major avg `0.3494` n `8`; equity avg `-0.1215` n `140`; fx avg `-0.0081` n `6`; index avg `-0.0662` n `26`; metal avg `-0.0164` n `20`; unknown avg `-0.1334` n `937`
- 4h: commodity avg `0.0758` n `12`; crypto_alt avg `1.0956` n `234`; crypto_major avg `0.6499` n `8`; equity avg `0.0787` n `140`; fx avg `-0.0506` n `6`; index avg `-0.0357` n `26`; metal avg `0.0166` n `20`; unknown avg `-0.2098` n `936`
- 24h: commodity avg `0.0796` n `12`; crypto_alt avg `2.2103` n `234`; crypto_major avg `0.7743` n `8`; equity avg `0.3798` n `140`; fx avg `-0.1818` n `6`; index avg `0.0053` n `26`; metal avg `0.1885` n `20`; unknown avg `1.0817` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
