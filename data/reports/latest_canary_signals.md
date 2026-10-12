# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T01:52:29.592177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `13`; crypto_alt avg `-0.2509` n `235`; crypto_major avg `-0.2282` n `8`; equity avg `-0.0125` n `150`; fx avg `-0.0111` n `6`; index avg `0.0237` n `26`; metal avg `0.0379` n `20`; unknown avg `1.0619` n `1134`
- 1h: commodity avg `-0.0927` n `13`; crypto_alt avg `-0.6028` n `235`; crypto_major avg `-0.3921` n `8`; equity avg `-0.0848` n `150`; fx avg `0.0006` n `6`; index avg `0.0131` n `26`; metal avg `0.024` n `20`; unknown avg `1.3325` n `1132`
- 4h: commodity avg `-0.4927` n `13`; crypto_alt avg `-0.2212` n `235`; crypto_major avg `0.0988` n `8`; equity avg `0.0007` n `150`; fx avg `-0.0404` n `6`; index avg `-0.002` n `26`; metal avg `0.0924` n `20`; unknown avg `0.7775` n `1110`
- 24h: commodity avg `-0.3422` n `13`; crypto_alt avg `0.9485` n `235`; crypto_major avg `0.5249` n `8`; equity avg `0.2337` n `150`; fx avg `-0.0375` n `6`; index avg `0.0264` n `26`; metal avg `0.1772` n `20`; unknown avg `0.9715` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
