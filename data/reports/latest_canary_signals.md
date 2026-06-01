# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T07:52:23.993037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1263` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.855` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0937` n `12`; crypto_alt avg `-0.3323` n `228`; crypto_major avg `-0.2036` n `8`; equity avg `-0.0934` n `69`; fx avg `0.0126` n `6`; index avg `-0.0375` n `23`; metal avg `-0.2289` n `18`; unknown avg `-0.3564` n `422`
- 1h: commodity avg `0.1869` n `12`; crypto_alt avg `-0.5294` n `228`; crypto_major avg `-0.6789` n `8`; equity avg `-0.1792` n `69`; fx avg `0.0391` n `6`; index avg `0.1179` n `23`; metal avg `-0.0871` n `18`; unknown avg `0.0125` n `422`
- 4h: commodity avg `0.5284` n `12`; crypto_alt avg `-2.204` n `228`; crypto_major avg `-1.5979` n `8`; equity avg `-0.3187` n `69`; fx avg `-0.0468` n `6`; index avg `0.2571` n `23`; metal avg `-0.1026` n `18`; unknown avg `-0.5624` n `412`
- 24h: commodity avg `1.3358` n `12`; crypto_alt avg `-0.3751` n `228`; crypto_major avg `-1.1334` n `8`; equity avg `-0.2285` n `69`; fx avg `-0.0079` n `6`; index avg `1.0111` n `23`; metal avg `-0.0955` n `18`; unknown avg `1.287` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2871`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
