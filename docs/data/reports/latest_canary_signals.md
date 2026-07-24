# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T14:22:35.107137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2286` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.2389` n `230`; crypto_major avg `-0.3224` n `8`; equity avg `-0.1558` n `100`; fx avg `0.0041` n `6`; index avg `0.0012` n `25`; metal avg `0.0266` n `20`; unknown avg `-0.1275` n `773`
- 1h: commodity avg `-0.1266` n `12`; crypto_alt avg `-0.4856` n `230`; crypto_major avg `-0.783` n `8`; equity avg `-1.9127` n `100`; fx avg `0.0092` n `6`; index avg `-0.1757` n `25`; metal avg `0.0539` n `20`; unknown avg `-0.2422` n `773`
- 4h: commodity avg `0.1356` n `12`; crypto_alt avg `-1.3934` n `230`; crypto_major avg `-1.4739` n `8`; equity avg `-2.3031` n `100`; fx avg `-0.0023` n `6`; index avg `-0.2453` n `25`; metal avg `-0.1312` n `20`; unknown avg `-0.276` n `773`
- 24h: commodity avg `-0.2847` n `12`; crypto_alt avg `-2.3354` n `230`; crypto_major avg `-2.3095` n `8`; equity avg `-3.2487` n `100`; fx avg `-0.1442` n `6`; index avg `-0.3851` n `25`; metal avg `-0.0982` n `20`; unknown avg `0.102` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1159`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1086`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1068`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0934`, n `666`, weak_sample_signal
